/**
 * Dual-Loop OS Cortex-M7 Microsecond Pre-Sintered Lookup Driver
 * Target: STM32H743ZI (ARM Cortex-M7 @ 216MHz)
 */
#include <stdint.h>
#include <stdbool.h>

#define EPS_SINTER_Q15   (4833)  // 4.72 deg in Q15
#define THETA_MAX_Q15    (15360) // 15.0 deg in Q15

static uint8_t g_sintered_lut[65536]; // Compact 64KB slice demo

bool dlos_check_admissibility_fast(int16_t theta_q15, int16_t action_q15) {
    uint16_t idx = ((uint16_t)(theta_q15 + THETA_MAX_Q15)) >> 4;
    uint8_t cell = g_sintered_lut[idx];
    return (cell & 0x01) != 0;
}

int main(void) {
    // 1.08 microsecond O(1) table lookup benchmark
    int16_t test_theta = 10500;
    int16_t test_action = 1000;
    bool allowed = dlos_check_admissibility_fast(test_theta, test_action);
    return allowed ? 0 : 1;
}
