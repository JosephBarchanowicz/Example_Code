--Written By: Joe Barchanowicz
--Binary Counter Test Bench

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity binary_counter_tb is
--  Port ( );
end binary_counter_tb;

architecture Behavioral of binary_counter_tb is

component binary_counter is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           pause : in STD_LOGIC;
           q : out STD_LOGIC_VECTOR (3 downto 0));
end component binary_counter;

signal clk_tb, rst_tb, pause_tb: std_logic; 
signal q_tb: std_logic_vector(3 downto 0);
signal cp: time:=10ns;

begin
uut: binary_counter port map(clk=>clk_tb, rst=>rst_tb, pause=>pause_tb, q=>q_tb);

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
