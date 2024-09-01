import xml

def main():
    import xml.etree.ElementTree as ET
    tree = ET.parse('country_data.xml')
  #  wb = load_workbook(filename = r'C:\Users\Ryzen\Downloads\dvdrental\Newfolder\actor.xlsx')


if __name__ == '__main__':
    main()


'''import sys
import trace

# create a Trace object, telling it what to ignore, and whether to
# do tracing or line-counting or both.
tracer = trace.Trace(
    ignoredirs=[sys.prefix, sys.exec_prefix],
    trace=1,
    count=1)

# run the new command using the given tracer
tracer.run('main()')

# make a report, placing output in the current directory
r = tracer.results()
r.write_results(show_missing=True, coverdir=".")'''


