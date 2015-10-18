#include "dr_api.h"
#include "drreg.h"
#include <stdio.h>


static void
event_exit(void) {
    dr_printf("Hi");
}

DR_EXPORT void
dr_client_main(client_id_t id, int argc, const char* argv[]) {
    dr_enable_console_printing();
    
    dr_register_exit_event(event_exit);
}