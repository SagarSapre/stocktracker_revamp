import requests

url = "https://www.nseindia.com/api/reports"

querystring = {"":"","archives":"[{\"name\":\"CM - Common Bhavcopy (csv)\",\"type\":\"archives\",\"category\":\"capital-market\",\"section\":\"equities\"}]","date":"23-Sep-2024","type":"equities","mode":"single"}

payload = ""
headers = {
    "cookie": "defaultLang=en; _ga=GA1.1.279452972.1724546327; _ga_87M7PJ3R97=GS1.1.1724546326.1.1.1724551084.44.0.0; nsit=zWRNwHy008AKI5UNvC1fY0-R; AKA_A2=A; _abck=F150EE5178F818BCDA870A4A6EAC7CA7~0~YAAQH/7UF22pycCRAQAAYJmk1AxO2EUcP7CbZM4B6Gb8XJwCYP+g3Fyq4o2ZkMfPQ3CQRf1ZHnuRAt9fBiAJYCrB1mLZ6G9Ee4Cs2pUyy7Jqqqh3apwMQIne2JL5VSJVkZdAqTMAcwM9DamTmAoQRbeiQ8BX2+Wo+1OsM3YPD5lp4BOD6CqhYZsJKQmU1RiNYmZmUAAEx+z82MxGR/FQNoJ12s3Qsja0AjfrO3WLy1R1/XAeuLFp3tdKRa30xoGpaigsqrA0SnfMaXBpFbcx3HhSqSAZB52QFfl+hiYWIwawjTnrWfa4CrY29s0pFoDNwqfdJhz8MRNQJMUsK28zMXwKdIhzGtXC3TXiiGyWQT5JZWrTrUZCC0NgiwiaxnKH6lYJ7vEgI508TMTj2b7loc4/awEWdBcSAYU=~-1~-1~-1; ak_bmsc=4A8844B03688FD9808BABCD6DD201C14~000000000000000000000000000000~YAAQH/7UF26pycCRAQAAYJmk1Bmpw5BGB7lqSwx8B5/vI3kamlRp14jQqR3Yrp6XHrhWkOPX2USLjlxHgk3Re2II+p5cLBuxhPB7+xLXFQZcI4h5PZ9+ShP6IzK2Ywg5uLS0gm9T1nq4G32qWWetC0IJglcKjlKbF1q9eXvuYiMlIo1LGG9WCx9M/SOhsZHEfkTKmcB76b9Ep1eHMU1hjRBnsV6b9jYvnYr43Y/X6dO69iS5ukGGWUZ78o8mSDXncMqICo/30RAzCLRxXlMl3wiRB+nL+nxttZloT8g3aqukdtdMXMme+MGCoyYcCCaFVUSiu4HhMDTaO0aWHzUQIRud28EoOBvCMgMecJIXl4+lQfuoDyTebwoYh1yTmI8gTD34uDO7l+QKoXA0MxQ=; nseappid=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJhcGkubnNlIiwiYXVkIjoiYXBpLm5zZSIsImlhdCI6MTcyNTg0OTQ1NSwiZXhwIjoxNzI1ODU2NjU1fQ.Xo128F5aQtSGAa7FS0nXKJIjW1n7IKqDwjW_a7kIGxc; bm_mi=330953332D465D0454FDA02A0F50034C~YAAQH/7UF4qqycCRAQAAlcuk1BlZ96CIQclEpIq0c6dz9jxvNVcVF9mzwljB7NTY9RZ0gEXf1PmHDncG7Kb0VRZnj4/0ok0UHrtlF0frqpYOaNrautgPvH21bxwqfd49IMHW+JpMKy/BJqtnoje2QthG8XWJrv59HgUs7+D6W8ajbTPP3aeHW2MW7HkjmEWqIQOzi5X3qCHwpMyl4qijIZIjO0WCzlxT+f+FiAqK+czn7OmcHK1wwDjLR4WG2se+/FeGee6ZKJXx19OrYWUSW61mknFwK0iPFDSdA46p2g2TvPdm3bKt3WiJjiSZtdbauYZ0vWFZMqY=~1; bm_sz=B3E004312E72076830A439F4682763E9~YAAQH/7UF4yqycCRAQAAlcuk1BlUQMPQ1ATt4cloorDIH4cpLjnLskjpgolPIz/UIreiLufxSDrRwmOb3QlYglhcBFfIpFgLsEI0fEjdNNrdYwm9lPkRzXluqxvxg0nrU64eEXBXi8NxUEgt++vcxBAPqHKrhmstJr/fF8rsSe+hn/IoUQdr0CtkcJY73Ll6+mudcsKUC0LAuNH9Qt+zHAutLmaSHGMSNNqxAKwaw2t/sHeK7/bQG4L+4BYuHliETV1ecXFeaIUZBK9q6SlrOePjs7BxMAxa5q981/ydflMVqIqTbRyLT/aDM1HGCGQ/VllSPvKeaymXSg+tijOfGJ6+cw049TMjoqxU3uX7uDb/idOOXe7hRhXzG9OZ14zTe4kTNJz/7wmpUgmhvUMOi+LhQ+tR1x8=~4539713~3355441; bm_sv=E9602B59348D779775E3025CD9E314F5~YAAQH/7UF1zwycCRAQAAD8us1BmdHiyeXCvfQeX2U0Et8HbyoQ+90B+6paHiEdx/0CSyJ3fbJz74Lt/ejHeWUQq5QCKLYPIFfmYerTXmFUUO9cNfny85lGbTb6Vr/7IJpH0/JsnNtWBVqA9qWxIo/ryCoY78w+mMYQwounhORMuqL1cY7LIX4TJ4SCjC6bQWUQJrsYrh50H3tstywm05tneD9e5h22ZRA3iBmit6xGA9gDfCGbljvtuZXLNbxnIr/pCw~1",
    "accept": "*/*",
    "accept-language": "en-US,en;q=0.9,hi;q=0.8",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "priority": "u=1, i",
    "referer": "https://www.nseindia.com/all-reports",
    "^sec-ch-ua": "^\^Chromium^^;v=^\^128^^, ^\^Not"
}

response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

print(response.text)