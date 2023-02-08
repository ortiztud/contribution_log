# Format your contributions
Do you have a long list of contribution to conferences that is getting hard to manage? Have you been requested to list all (or some) of them with a specific format? _I got you covered_.

This repo contains a small script that will take in a .csv with your contributions (`contribution_list.csv`) and will output them with a nice format ('formatted_contributions.txt). The default format is:

`{authors} ({year}). {title}. {acronym}. {organizer}. {city} ({country}). {contribution_type}"`

Feel free to adjusted to fit your needs (lines 33-36).

The script expects the input file to be in the same directory as the script (i.e., the root directory). Under the `examples` folder you can find a test example. If you want to try it out, just copy the `contribution_list.csv` file to the root directory.


_Powered by ChatGPT_
