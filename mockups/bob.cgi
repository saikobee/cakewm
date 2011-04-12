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
            cgi.body{yield}
        end
    end
end

def mn_table m, n, cgi=$cgi
    selection = [1, 0]
    cgi.table{
        (0 ... m).map{|x|
            cgi.tr{
                (0 ... n).map{|y|
                    classes = []
                    classes << "right"      if y == (n - 1)
                    classes << "bottom"     if x == (m - 1)
                    classes << "selected"   if [x, y] == selection
                    classes = classes.join " "

                    cgi.td(:class => classes){yield}
                }.join
            }
        }.join
    }
end

table = mn_table(4, 4){"foobar"}

za_warudo do
    table +
    cgi.h1{"cakewm for life"} +
    cgi.h2{"best wm ever"} +
    cgi.h3{"love it so much"} +
    cgi.h4{"saiko cake factory"} +
    cgi.h5{"bad ugly text"}
end
