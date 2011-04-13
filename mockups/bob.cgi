#!/usr/bin/ruby

require "cgi"

$cgi = cgi = CGI.new("html4")

def header cgi=$cgi
    cgi.head do
        cgi.title{"cakewm table mockup thingy"} +
        cgi.link(
            :rel  => "stylesheet",
            :type => "text/css",
            :href => "bob.css"
        )
    end
end

def za_warudo cgi=$cgi
    cgi.out do
        cgi.html do
            header +
            cgi.body { yield }
        end
    end
end

def mn_table m, n, cgi=$cgi
    selection = [1, 0]
    cgi.table {
        make_bar("top", m) +
        (0 ... n).map {|x|
            cgi.tr {
                (0 ... m).map {|y|
                    classes = []
                    classes << "right"  if y == (n - 1)
                    classes << "bottom" if x == (m - 1)
                    classes << "left"   if y == 0
                    classes << "top"    if x == 0
                    classes = classes.join " "

                    cgi.td(:class => classes) { yield x, y }
                }.join
            }
        }.join +
        make_bar("bottom", m)
    }
end

def make_bar edge, width, cgi=$cgi
    bot_text =
        cgi.div(:class => "left" ) { "(Window Title)" } +
        cgi.div(:class => "right") { "(P, Q) MxN (A/B)" }
    top_text =
        cgi.div(:class => "left" ) { "(Desktop List)" } +
        cgi.div(:class => "right") { "(Infobar Text)" }

    cgi.tr {
        cgi.td(
            :class   => "bar #{edge}",
            :colspan => width
        ) {
            case edge
            when "top";     top_text
            when "bottom";  bot_text
            else            "ERROR TEXT"
            end
        }
    }
end

table = mn_table(3, 4) {|x, y|
    cgi.div(:class => "inner") {
        "(#{x}, #{y})"
    }
}

def make_table title, table, cgi=$cgi
    cgi.table {
        cgi.th { title } +
        table.map {|row|
            cgi.tr {
                row.map {|item|
                    cgi.td {
                        item
                    }
                }.join
            }
        }.join
    }
end

definitions = make_table "Definitions", [
    ["(P, Q)",  "Window's top-left is at grid-square (P, Q)"],
    ["MxN",     "Window is MxN grid squares in area"],
    ["(A/B)",   "Window is #A out of B items in stack"],
]

za_warudo do
    table +
    definitions
end
