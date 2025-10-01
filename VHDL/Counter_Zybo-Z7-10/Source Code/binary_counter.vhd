--Written By: Joe Barchanowicz
--Binary Counter

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity binary_counter is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           pause : in STD_LOGIC;
           q : out STD_LOGIC_VECTOR (3 downto 0));
end binary_counter;

architecture Behavioral of binary_counter is

signal count: unsigned(3 downto 0):=(others=>'0');

begin

q <= std_logic_vector(count);

process(clk,rst)
begin
    if(rst='1') then
        count <= (others=>'0');
    elsif(rising_edge(clk)) then
        if(pause='1') then
            count <= count;
        else
            count <= count+1;
        end if;
     end if;
end process;
end Behavioral;