# An Iris Reanalysis Data package (IRData)

 SciTools/Iris provides a data structure for GCM weather data, and tools for file IO. I want to go beyond that and have an API for loading the particular weather data I need into an iris Cube. That is, to say something like:

'from the CERA20C reanalysis, load the 2m air temperature at 7am (UTC) on 16th October 1987.`

and the code would find and download the data, interpolating to the requested time as necessary. IRData provides such an API, for synoptic-timescale reanalysis data, from several reanalyses. The request above is:

```
    import datetime
    dtime=datetime.datetime(1987,10,16,7)
    import IRData.cera20c as cera20c
    cera20c.fetch('air.2m',dtime)
    mycube=cera20c.load('air.2m',dtime)
```

There is one sub-package for each of several data sources, with `fetch` methods for getting a copy of the data from a remote server to a local filesystem. and `load` methods for loading iris cubes from the fetched data. 

1.  IRData.twcr - Data from the 20th Century Reanalysis.
2.  IRData.cera20c - Data from the CERA20C Reanalysis.
3.  IRData.era5 - Data from the ERA5 Reanalysis.

See [the docs](http://brohan.org/IRData/).

This is a personal software library; it builds on SciTools/Iris and is licensed on the same terms, but it does not have the same level of documentation, support, testing, or stability.


