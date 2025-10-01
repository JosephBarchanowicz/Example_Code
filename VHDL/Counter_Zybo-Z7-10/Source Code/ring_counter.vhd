--Written By: Joe Barchanowicz
--Ring Counter

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity ring_counter is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           pause : in STD_LOGIC;
           q : out STD_LOGIC_VECTOR(3 downto 0));
end ring_counter;

architecture Behavioral of ring_counter is

signal count: std_logic_vector(3 downto 0):=(others=>'0');

begin

process(clk,rst) 
begin
if(rst='1') then
    count(3) <= '1';
    count(2) <= '0';
    count(1) <= '0';
    count(0) <= '0';
elsif(rising_edge(clk)) then 
    if(pause='1') then
        count <= count;
    else 
        count(3) <= count(0);
        count(2) <= count(3);
        count(1) <= count(2);
        count(0) <= count(1);
    end if;
end if;
end process; 

q <= count;

end Behavioral;
