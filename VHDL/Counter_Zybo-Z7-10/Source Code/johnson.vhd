--Written By: Joe Barchanowicz
--Johnson Counter

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
 
entity johnson is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           pause : in STD_LOGIC;
           q : out STD_LOGIC_VECTOR (3 downto 0));
end johnson;
 
architecture Behavioral of johnson is

signal temp: std_logic_vector(3 downto 0):= "0000";

begin

process(clk,rst)
begin
    if rst = '1' then
        temp <= "0000";
    elsif rising_edge(clk) then
        if pause = '1' then
            temp <= temp;
        else
            temp(2) <= temp(3);
            temp(1) <= temp(2);
            temp(0) <= temp(1);
            temp(3) <= not temp(0);
        end if;
    end if;
end process;

q <= temp;

end Behavioral;

