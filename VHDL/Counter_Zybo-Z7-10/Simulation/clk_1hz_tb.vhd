--Written By: Joe Barchanowicz
--1Khz Clock Test Bench

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity clk_1hz_tb is
--  Port ( );
end clk_1hz_tb;

architecture Behavioral of clk_1hz_tb is

component clk_1hz is
    Port ( clk : in STD_LOGIC;
           clk_output : out STD_LOGIC );
end component clk_1hz;

signal clk_tb : STD_LOGIC;
signal clk_output_tb : STD_LOGIC;

constant CP : time := 20ns;

begin

UUT: clk_1hz port map (clk => clk_tb, clk_output => clk_output_tb);

process begin 
    clk_tb <= '1';
    wait for CP/2;
    clk_tb <= '0';
    wait for CP/2;
end process; 

end Behavioral;
