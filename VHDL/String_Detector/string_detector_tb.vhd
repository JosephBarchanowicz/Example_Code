-- Written By: Joe Barchanowicz 
-- String Detector Test Bench

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity string_detector_tb is
--  Port ( );
end string_detector_tb;

architecture Behavioral of string_detector_tb is

component string_detector is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           x : in character;
           y : out STD_LOGIC);
end component string_detector;

signal clk_tb, rst_tb, y_tb : std_logic;
signal x_tb : character;

constant CP : time := 10 ns;

begin
UUT: string_detector port map (clk => clk_tb, rst => rst_tb, x => x_tb, y => y_tb);

process
begin
    clk_tb <= '1';
    wait for CP/2;
    clk_tb <= '0';
    wait for CP/2;
end process;

process
begin
    rst_tb <= '1';
    wait for 10 ns;
    rst_tb <= '0';
    wait;
end process;

process
begin
    x_tb <= 'a';
    wait for 20ns;
    x_tb <= 'b';
    wait for 20ns;
    x_tb <= 'c';
    wait for 20ns;
    x_tb <= 'A';
    wait for 20ns;
    x_tb <= 'a';
    wait for 20ns;
    x_tb <= 'B';
    wait for 20ns;
    x_tb <= 'a';
    wait for 20ns;
    x_tb <= 'b';
    wait for 20ns;
    x_tb <= 'c';
    wait for 20ns;
end process;

end Behavioral;
