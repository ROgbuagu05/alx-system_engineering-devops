#!/usr/bin/env ruby
# Ruby script that accepts one argument

regex = /School/
puts ARGV[0].scan(regex).join
