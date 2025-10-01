--Written By: Joe Barchanowicz
--4x1 Multiplexer

library IEEE;
use IEEE.STD_LOGIC_1164.ALL;

entity mux_4to1 is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           pause : in STD_LOGIC;
           sel : in STD_LOGIC_VECTOR (1 downto 0);
           output : out STD_LOGIC_VECTOR (3 downto 0));
end mux_4to1;

architecture Behavioral of mux_4to1 is

component binary_counter is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           pause : in STD_LOGIC;
           q : out STD_LOGIC_VECTOR (3 downto 0));
end component binary_counter;

component ring_counter is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           pause : in STD_LOGIC;
           q : out STD_LOGIC_VECTOR(3 downto 0));
end component ring_counter;

component johnson is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           pause : in STD_LOGIC;
           q : out STD_LOGIC_VECTOR (3 downto 0));
end component johnson;

component fibonacci is
    Port ( clk : in STD_LOGIC;
           rst : in STD_LOGIC;
           pause : in STD_LOGIC;
           q : out STD_LOGIC_VECTOR (3 downto 0));
end component fibonacci;

signal out_00, out_01, out_10, out_11, out_temp : STD_LOGIC_VECTOR (3 downto 0);

begin
comp00 : binary_counter port map (clk => clk, rst => rst, pause => pause, q => out_00);
comp01 : ring_counter port map (clk => clk, rst => rst, pause => pause, q => out_01);
comp10 : johnson port map (clk => clk, rst => rst, pause => pause, q => out_10);
comp11 : fibonacci port map (clk => clk, rst => rst, pause => pause, q => out_11);

process (clk, sel) is
begin
  if (sel = "00") then
      out_temp <= out_00;
  elsif (sel = "01") then
      out_temp <= out_01;
  elsif (sel = "10") then
      out_temp <= out_10;
  else
      out_temp <= out_11;
  end if;
end process;

output <= out_temp;

end Behavioral;
