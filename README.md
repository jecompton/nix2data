nix2data is a suite of scripts that take output piped from the stdout of various
Unix/Linux command line utilities, parses it, and produces more the data in a
more uniform format (e.g., json, csv).

These utilities often are not meant to be parsed such as `ls`, `ps`, and more.
We're going to do it anyway. For decades, many systems-working souls have used
grep/sed/awk more or less happily to parse this output to get what they need.
These tools will help ease this sort of usage.

Of course there are good reasons not to use these tools for serious automation
and integration with production systems. Know that YMMV, but I hope these
scripts will help if you don't have a better solution readily available.

The typical usage of a script looks something like this:
```
lsblk | lsblk2data.py
```

What you get is valid json of (in this case) your storage devices so you can put
the data in some visualization tool, stash it in some data store, or email it to
your most intimate of associates.


## Language(s) used

In the early period of this repo, I may use a hodge-podge of languages and tools
that best fit the particular problem. I will likely favor Python since it is
cleaner than bash for doing work with things like JSON and can be expected to
exist on most major \*nixes. I love Ruby, Javascript >= es6, and other
languages, but Python hits a sweet spot for systems work, portability, and data
science work.

Who knows? Some day there might be some Rust versions of these that are safer
and faster.
