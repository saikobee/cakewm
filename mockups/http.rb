#!/usr/bin/ruby

require "webrick"
include  WEBrick

server = HTTPServer.new(
    :Port           => 1234,
    :DocumentRoot   => "."
)

# Cleanly exit the program upon SIGINT and SIGTERM
[:INT, :TERM].each do |signal|
    trap signal do
        server.shutdown
    end
end

server.start
