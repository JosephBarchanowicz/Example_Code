-- Written By: Joe Barchanowicz 
-- String Detector



library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

-- Uncomment the following library declaration if using
-- arithmetic functions with Signed or Unsigned values
--use IEEE.NUMERIC_STD.ALL;

-- Uncomment the following library declaration if instantiating
-- any Xilinx leaf cells in this code.
--library UNISIM;
--use UNISIM.VComponents.all;

entity string_detector is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           x : in character;
           y : out STD_LOGIC);
end string_detector;

architecture Behavioral of string_detector is

type state is (idle, char1, char2, char3);
signal cur_state, next_state : state;

begin
process(clk, rst)
begin
    if(rising_edge(clk)) then
        if(rst = '1') then
            cur_state <= idle;
            --y <= '0';
        else
            cur_state <= next_state;
        end if;
    end if;
end process;

process(x)
begin
    case cur_state is
        when idle => 
            if (x = 'a') then
                next_state <= char1;
                y <= '0';
            else
                next_state <= idle;
                y <= '0';
            end if;
        when char1 =>
            if (x = 'b') then
                next_state <= char2;
                y <= '0';
            else
                next_state <= idle;
                y <= '0';
            end if;
        when char2 =>
            if (x = 'c') then
                next_state <= char3;
                y <= '0';
             else
                next_state <= idle;
                y <= '0';
             end if;
         when char3 =>
            if (x = 'a') then
                next_state <= char1;
                y <= '1';
            else
                next_state <= idle;
                y <= '1';
            end if; 
    end case; 
end process;
end Behavioral;
