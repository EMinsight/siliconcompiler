
`default_nettype none

module heartbeat #(
    parameter N = 8
) (
    //`ifdef USE_POWER_PINS
    inout vpp,  // User area 1 1.8V supply
    inout gnd,  // User area 1 digital ground
    //`endif

    //inputs
    input      clk,     // clock
    input      nreset,  //async active low reset
    output reg out      //heartbeat

);

    reg [N-1:0] counter_reg;

    always @(posedge clk or negedge nreset)
        if (!nreset) begin
            counter_reg <= 'b0;
            out <= 1'b0;
        end else begin
            counter_reg[N-1:0] <= counter_reg[N-1:0] + 1'b1;
            out <= (counter_reg[N-1:0] == {(N) {1'b1}});
        end

endmodule
`default_nettype wire
