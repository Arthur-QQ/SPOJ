defmodule Addrev do
    def func(n) do
        if n > 0 do
            {a, b} = IO.gets("") |>
            String.slice(0..-2) |>
            String.split |>
            Enum.map(fn x -> x |> String.reverse |> String.to_integer end) |>
            List.to_tuple
            c = a + b
            c |>
            Integer.to_string |>
            String.reverse |>
            String.to_integer |>
            IO.puts
            func(n - 1)
        else
            ""
        end
    end
    def main do
        IO.gets("") |>
        String.slice(0..-2) |>
        String.to_integer |>
        func
    end
end

Addrev.main
