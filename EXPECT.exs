defmodule Expect do
 def read_integer do
  b = IO.gets ""
  String.slice(b, 0, String.length(b)-1)
 end
 def main do
  a = read_integer() |> String.to_integer
  IO.puts a
  if a != 42 do
   main()
  else
   :nil
  end
 end
end

Expect.main
