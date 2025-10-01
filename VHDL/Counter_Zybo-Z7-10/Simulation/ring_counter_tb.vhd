--Written By: Joe Barchanowicz
--Ring Counter Test Bench

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity ring_counter_tb is
--  Port ( );
end ring_counter_tb;

architecture Behavioral of ring_counter_tb is

component ring_counter is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           pause : in STD_LOGIC;
           q : out STD_LOGIC_VECTOR(3 downto 0));
end component ring_counter;

signal clk_tb, rst_tb, pause_tb: std_logic; 
signal q_tb: std_logic_vector(3 downto 0);
signal cp: time:=10ns;

begin
uut: ring_counter port map(clk=>clk_tb, rst=>rst_tb, pause=>pause_tb, q=>q_tb);

process --clk
begin
clk_tb<='1';
wait for cp/2;
clk_tb<='0';
wait for cp/2;
end process;

process --rst
begin
rst_tb <= '1';
pause_tb<='0';
wait for cp;
rst_tb <= '0';
wait for 100ns;
pause_tb<='1';
wait for cp;
pause_tb<='0';
wait;
end process;


end Behavioral;