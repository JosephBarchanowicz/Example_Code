--Written By: Joe Barchanowicz
--Top Level

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity top_level is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           pause : in STD_LOGIC;
           sel : in STD_LOGIC_VECTOR (1 downto 0);
           output : out STD_LOGIC_VECTOR (3 downto 0));
end top_level;

architecture Behavioral of top_level is

component mux_4to1 is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           pause : in STD_LOGIC;
           sel : in STD_LOGIC_VECTOR (1 downto 0);
           output : out STD_LOGIC_VECTOR (3 downto 0));
end component mux_4to1;

component clk_1hz is
    Port ( clk : in STD_LOGIC;
           clk_output : out STD_LOGIC );
end component clk_1hz;

signal clk1hz : STD_LOGIC;

begin

comp_clk: clk_1hz port map (clk => clk, clk_output => clk1hz);
comp_mux: mux_4to1 port map (clk => clk1hz, rst => rst, pause => pause, sel => sel, output => output);

end Behavioral;
