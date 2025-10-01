--Written By: Joe Barchanowicz
--1KHz Clock

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity clk_1hz is
    Port ( clk : in STD_LOGIC;
           clk_output : out STD_LOGIC );
end clk_1hz;

architecture Behavioral of clk_1hz is

signal clk_temp : STD_LOGIC := '0';
signal count : INTEGER := 0;

begin  

process(clk)
begin
    if rising_edge (clk) then
        count <= count + 1;
        if count = 24999999 then
            clk_temp <= not clk_temp;
            count <= 0;
        end if; 
    end if;  
end process;
clk_output <= clk_temp;

end Behavioral;
