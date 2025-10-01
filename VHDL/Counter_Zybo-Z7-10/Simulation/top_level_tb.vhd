--Written By: Joe Barchanowicz
--Top Level Test Bench

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity top_level_tb is
--  Port ( );
end top_level_tb;

architecture Behavioral of top_level_tb is
component top_level is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           pause : in STD_LOGIC;
           sel : in STD_LOGIC_VECTOR (1 downto 0);
           output : out STD_LOGIC_VECTOR (3 downto 0));
end component;

signal clk_tb, rst_tb, pause_tb : STD_LOGIC;
signal sel_tb : STD_LOGIC_VECTOR (1 downto 0);
signal output_tb : STD_LOGIC_VECTOR (3 downto 0);

constant CP : time := 10ns;

begin

UUT: top_level port map (clk => clk_tb, rst => rst_tb, pause => pause_tb, sel => sel_tb, output => output_tb);

process begin 
    clk_tb <= '1';
    wait for CP/2;
    clk_tb <= '0';
    wait for CP/2;
end process; 

process begin 
    sel_tb <= "00";
    rst_tb <= '1';
    pause_tb <= '0';
    wait for CP;
    rst_tb <= '0';
    wait for 100 ns;
    pause_tb <= '1';
    wait for 50 ns;
    pause_tb <= '0';
    wait for 100 ns;
    sel_tb <= "01";
    rst_tb <= '1';
    pause_tb <= '0';
    wait for CP;
    rst_tb <= '0';
    wait for 100 ns;
    pause_tb <= '1';
    wait for 50 ns;
    pause_tb <= '0';
    wait for 100 ns;
    sel_tb <= "10";
    rst_tb <= '1';
    pause_tb <= '0';
    wait for CP;
    rst_tb <= '0';
    wait for 100 ns;
    pause_tb <= '1';
    wait for 50 ns;
    pause_tb <= '0';
    wait for 100 ns;
    sel_tb <= "11";
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
