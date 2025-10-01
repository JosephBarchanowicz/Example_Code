--Written By: Joe Barchanowicz
--Fibonacci Counter Test Bench

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity fibonacci_tb is
--  Port ( );
end fibonacci_tb;

architecture Behavioral of fibonacci_tb is

component fibonacci is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           pause : in STD_LOGIC;
           q : out STD_LOGIC_VECTOR (3 downto 0));
end component fibonacci;

signal clk_tb, rst_tb, pause_tb : std_logic;
signal q_tb : std_logic_vector (3 downto 0);

constant CP : time := 10ns;

begin

uut: fibonacci port map (clk => clk_tb, rst => rst_tb, pause => pause_tb, q => q_tb);

process begin 
    clk_tb <= '1';
    wait for CP/2;
    clk_tb <= '0';
    wait for CP/2;
end process;

process begin 
    rst_tb <= '1';
    pause_tb <= '0';
    wait for CP;
    rst_tb <= '0';
    wait for 100 ns;
    pause_tb <= '1';
    wait for 30 ns;
    pause_tb <= '0';
    wait;
end process;

end Behavioral;
