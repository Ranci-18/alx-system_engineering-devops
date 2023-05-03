#!/usr/bin/env ruby
#Ruby script accepts one argument and passes it to a
#regular expression mathching method

puts ARGV[0].scan(/hbt*n/).join
