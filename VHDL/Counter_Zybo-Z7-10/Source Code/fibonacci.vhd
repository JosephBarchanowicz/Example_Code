--Written By: Joe Barchanowicz
--Fibonacci Counter

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.NUMERIC_STD.ALL;

entity fibonacci is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           pause : in STD_LOGIC;
           q : out STD_LOGIC_VECTOR (3 downto 0));
end fibonacci;

architecture Behavioral of fibonacci is

signal a,b,c : integer range 0 to 16;

begin

process	(clk, rst)	
begin
    if (rst = '1') then
        b <= 1;	
        c <= 0;	
    elsif (clk'event and clk = '1') then
        if pause = '1' then
            c <= c;
            b <= b;
            a <= a;
        elsif (c < 13) then
		    c <= b;	
            b <= a;
        else
            a <= 0;
            b <= 1;	
            c <= 0;
        end if;   	
	end if;
a <= b + c;

end process;

q <= std_logic_vector(to_signed(c, 4));

end Behavioral;
