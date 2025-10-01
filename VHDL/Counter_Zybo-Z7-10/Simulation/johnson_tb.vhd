--Written By: Joe Barchanowicz
--Johnson Counter Test Bench

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity johnson_tb is
--  Port ( );
end johnson_tb;

architecture Behavioral of johnson_tb is

component johnson is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           pause : in STD_LOGIC;
           q : out STD_LOGIC_VECTOR (3 downto 0));
end component johnson;

signal clk_tb, rst_tb, pause_tb : std_logic;
signal q_tb : STD_LOGIC_VECTOR (3 downto 0);

constant CP : time := 10 ns;

begin

uut: johnson port map (clk => clk_tb, rst => rst_tb, pause => pause_tb, q => q_tb);

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
    wait for 50 ns;
    pause_tb <= '0';
    wait;
end process;

end Behavioral;
