**I.REQUIREMENTS**

**1.Terms**  
Fuzzing genealogy and even the term “fuzz” originates from a researcher at the University of Wisconsin, Madison named Barton Miller. In the mid to late eighties, Professor Miller observed that thunderstorms caused line noise in his modem connection to remote computers. This line noise periodically injected junk characters into the remote sessions causing interference with program operation. Eventually, programs crashed due to these junk characters, and, Professor Miller coined the term “fuzz” to describe this behavior  

**2.Requirements for Fuzzer (Sutton et al. and Takanen et al.)**  
**2.1.Document test cases:  Guarantee reproducibility**  
Test case documentation informs a researcher of a negative test case’s storage location, time at which a program ran the test case, and the result of executing a program with the test case. This documentation guarantees that the observed behavior can be reliably reproduced. If a negative test case is not properly documented and stored, then a crash caused by it is incapable of being reproduced or analyzed. Improper documentation and storage can also cause a higher false positive rate. In this context, a false positive indicates a negative test case causes a program exception when in actuality program execution terminates normally.  

**2.2.Monitor a program under test: provide informative metrics**  
Process monitoring tracks a program’s state during the execution of a negative test case. Information collected from the monitoring serves as historical data about program behavior. The historical data can then be aggregated to generate useful metrics, such as code coverage. Various forms of code coverage metrics exist like branch coverage. This metric calculates the number of branches executed by a test case out of the total number of branches within a program [Beizer]. For completeness, a branch is a program decision point where execution can proceed in more than one alternative. Accurate and relevant metrics, like branch coverage,are helpful in determining the amount of code tested by a fuzzer.  

**2.3.Properly detect program exceptions:**  
	Error detection, also known as exception monitoring or health monitoring, determines a program’s reaction to a test case by examining process state after execution ceases. A monitor evaluates process state for abnormal exit conditions like segmentation violations, bus errors, and arithmetic exceptions among many others. The fidelity of an exception monitor impacts the rate of false positives as well as false negatives. A false negative states a test case causes a program 
to exit normally when, in reality, the test case causes an exception. Issues about exception monitoring fidelity are important to consider while developing or evaluating a fuzzer.

**2.4.Exception analysis**  
	Takanen et al. extend upon Sutton’s requirements by encouraging the addition of exception analysis. Exception analysis combines information gathered during process and exception monitoring to determine the cause and impact of an observed exception. The effort required for this analysis is dependent upon the level of detail obtained from process and exception monitoring. Exceptions,also referred to as program faults, have underlying defects ranging in severity from  benign Denial Of Service (DoS) to catastrophic remotely exploitable memory corruption. Defects resulting in DoS are less severe than remotely exploitable defects, because it is infeasible to run arbitrary malicious code. With remotely exploitable defects, an attacker may be capable of exploiting the defect and assuming full control of the running process. To determine a defect’s cause and severity, exception analysis can be conducted by rerunning a test case with a debugger connected
to the program under test, inserting special debugging shared libraries (e.g. libgmalloc), or by running third party utilities to parse and interpret error logs (e.g. !exploitable or crashwrangler). A determination of cause and severity derived from exception analysis informs a developer of a defect’s impact to a program’s customers.

**II. Fuzzer's Design**  
**1.Fuzzer classification**
	Fuzzer classification primarily relies on a dissection of a fuzzer’s algorithm for generating negative test cases.
	There're three types of fuzzer:
		- Mutation fuzzer
		- Generation fuzzzer
		- Feedback fuzzer
	Mutation fuzzers were the only classification until the turn of the 21st century when generation fuzzers were introduced. Only recently, over the past five years (from 2010), feedback fuzzers have debuted and increased in prevalence.

**2. Fuzzer's core components**  
**2.1. Attack heuristics:** Define the set of anomalous data to be inserted by a fuzzer into a test case. More formally, attack heuristics are techniques proven to find defects in applications by past experiences [Takanen et al. 2008].
	These techniques could be random, such as sampling from /dev/urandom, inserting historically known troublesome values, or any combination thereof. An instance of known troublesome values are boundary conditions of basic types. For instance, the maximum value of an 8-bit unsigned char or a 16-bit unsigned short may be members of an attack heuristic set. These values, 255 and 65,535, are in the attack heuristics of several fuzzers and may cause programs to crash [Amini 
and Portnoy 2007, Eddington 2006] . A fuzzer, either randomly or systematically, selects values from this set and inserts the selected value into a negative testcase. The quality and number of attack heuristics can impact the ability of a fuzzer to find defects.  

**2.2. Executor:** An executor is the mechanism a fuzzer uses to run a program under test and deliver a generated negative test case.
	Executor design depends on several factors such as the programs intended to be tested, input vectors, and operating system. An input vector is the avenue 
which data is presented to an application for processing. Two common input vectors are network traffic and files.
	Executor design is dependent on multiple factors, because different programs and operating systems handle input vectors in different manners. For instance, if a program under test accepts command line arguments to select file input and the designated input vector to fuzz is file parsing, Executor design is dependent on multiple factors, because different programs and operating systems handle input vectors in different manners. For instance, if a program under test accepts
command line arguments to select file input and the designated input vector to fuzz is file parsing, then an executor only requires running a program with the correct command line arguments and negative test case. In another instance, a program may not accept command line arguments to specify file input. The lack of a command line argument for file input increases executor complexity, since the executor must present the file through a different method. One way this can be achieved on the Mac OS X operating system is through the Applescript language. This scripting language controls scriptable applications with actions like file opening, program closing, and file saving among many others. A well designed executor accounts for differences in program operation and presents robust cross-platform interaction and control [Apple Script].

**2.3. Monitor:**   
A monitor or health monitor watches the program under test in an effort to determine the outcome from running a negative test case.  
	As with an executor, the target application and, to a larger degree, the operating system determines the method of monitoring. Several different methods exist to reliably monitor and detect application faults. A program under test can be monitored by starting the process with an attached debugger. The debugger automatically catches faults generated by an application, and, the debugger provides detailed information about a fault. Monitoring with a debugger can also be achieved with scriptable interfaces like the popular Python library pydbg [Amini 2006] or the newly released Ruby library Ragweed [Monti et al.]. Scriptable interfaces are convenient, but unfortunately, they can be platform dependent.
	Another option for monitoring is to detect the operating system writing to an error log. One example, on Mac OS X, is the directory ~/Library/Logs/CrashReporter. If a monitor watches this directory for changes, then it can detect program faults. However, since directory watching does not monitor program execution, the information collected by this method is not as detailed as monitoring with a debugger. Error directory or file watching is also platform dependent in terms of the files to watch and the different watching interfaces. This platform dependency is evident when comparing Linux and Mac OS X. For Linux, directories and files are capable of being watched with the inotify library, and for Mac OS X, a program can register to receive notifications of directory changes through the FSEvents API
	Another, more heavy-weight monitoring option, is to emulate the program under test with a Dynamic Binary Instrumentation Framework (DBI). These frameworks translate native instructions into an intermediate representation thereby providing hooks for developers to interact directly with the translation during execution. The translated instructions are instrumented based on the programmer hooks, and then the intermediate representation is executed. Since the DBI 
translates every instruction and executes the translation, every detail about execution can be gathered. Faults are capable of being detected in real-time and detailed information about execution can be logged.

**2.4. Logger:**  
 A logger records fuzzer progress with a log of fuzzer events which can be audited later. The log contains details such as the time each negative 
test case is generated, location of a negative test case, and any fuzzer specific debugging information. 
	A logger can also catalog fuzzer configurations and start and stop times for performance comparisons. Logs created by the logger aid a tester in fuzzer 
development and auditing fuzzer results. Logs are the primary resource for debugging and historical data.

**2.5. Reporters:**   
Reporters summarize pertinent information on demand about a fuzzer run and notify a tester of important events
	Summary information includes the number of test cases executed, current runtime, and the current list of test cases causing faults. A notable event for the reporter is a program generating an exception from a test case. Instant program crash notification provides instant feedback about the fuzzer’s attack heuristics and algorithm. Loggers and reporters are similar, yet a reporter is distinguishable by its on demand summarization and instant notification. By contrast, a logger records more detailed information for later review after a fuzzer concludes testing.  

**3. Fuzzer's extended components**  
Fuzzers implementing only the core components are classifiable as mutation fuzzers. Mutation fuzzing, synonymous with dump fuzzing, is the earliest 
classification developed by Barton Miller. These fuzzers generate negative test cases by mutating sample inputs with attack heuristics.  

**3.1. Modelers (Generation fuzzer):**   
A modeler is an API for specifying a test case’s format
	The next category of fuzzing, generation or intelligent fuzzing, increases complexity by adding a modeling component to the set of core components. 
	Modeling APIs vary widely and are dependent upon a generation fuzzer’s implementation. One fuzzer may define C functions to represent different formats, and
another fuzzer may define a modeling language with an expressive markup language like Extensible Markup Language (XML).

**3.2. Search Algorithm, Learning Algorithm (Feedback fuzzer)**  
A feedback fuzzer evaluates software from a search space optimization view point with information from static and dynamic binary analysis. Static binary analysis interprets compiled code by extracting program characteristics. Tools, such as IDA Pro or objdump, handle converting a binary representation to intelligible assembly code. Dynamic analysis monitors a running program to profile execution. It is achieved through DBI frameworks like DynamoRIO, PIN, and Valgrind or other debugging interfaces.  
Information obtained about code structure and flow from static and dynamic analysis are fed into common search space algorithms such as genetic algorithms or constraint solvers. The fuzzer makes informed decisions about future test cases based upon the feedback from analysis of a currently running test case. The algorithms try to pinpoint problematic values in particular test cases or optimize metrics such as code coverage. These attempts to optimize metrics or solve constraints are an effort to minimize the number of negative test cases generated in order to find a defect.
