# share-file-qr

![PyPI](https://img.shields.io/pypi/v/share-file-qr.svg)

Share files from the terminal of your computer to a smartphone by scanning a QR code.

This repo is a Python re-implementation of the original [Go version](https://github.com/claudiodangelis/qr-filetransfer)
by [Claudio d'Angelis](https://claudiodangelis.com/).

## Installation

Fancy installation (recommended):
* `pipsi install share-file-qr`

Pip installation:
* `pip install share-file-qr`

## Principle

The principle is the same as in the Go version:
1. you give a file to the tool
2. the tool serves this file with HTTP server
3. the tool gives you a QR code leading to the URL pointing to the server
   and the file on the local network
4. you scan the QR code with your smartphone and get the URL to your file
5. you open the URL with your smartphone's web browser, and download starts
6. you stop the tool

## Usage

First, make sure your computer and your smartphone are connected to the same local
network. This is in general the case if they are connected to the same Wifi box. If you
have doubts, check their IP addresses. Please also be aware that this tool does not
work with IPv6.

Once connectivity issues are solved, run the tool by providing a file:

```
➜ share-file-qr README.md 

    █▀▀▀▀▀█  █ █▄  ▀▀▄▄ █ █▀▀▀▀▀█    
    █ ███ █ █▄▀▄█ ▀ █ ▀█▀ █ ███ █    
    █ ▀▀▀ █ █ ██▀███▄ ▀▀▄ █ ▀▀▀ █    
    ▀▀▀▀▀▀▀ █▄█ ▀▄▀▄▀ ▀ █ ▀▀▀▀▀▀▀    
    ▀ ▀█▀▀▀▄▄█▀▄  ▀█▄ ▄▄▄ █▀███▄▄    
    █▄█▄▀▀▀▀▄█▀▀  ▄ ▄ ▀ ▄▄    ▀█▄    
    ██▀▀██▀█ ▄▀▄▀▄▄▄▀ ▄█▄▀▄▀▄▀▀▀▄    
    █▀▀███▀█▀▄ ▄██▀█▀ ▄ ▀█  ▄▀ ▀     
    █▀▄█  ▀ ▀ ▄▄█ ▀█▄▄▄█▄▀▄▀▄█▀▀█    
    █  ▀▄ ▀▄██▀▄  ▄ ▄  ▄▄█ ▄  ▀▀     
    ▀ ▀   ▀▀█▄█▄▀▄▄▄  ▄ █▀▀▀█▀█▀▄    
    █▀▀▀▀▀█ ▄▀▄▀ █▀█▄  ██ ▀ █  ▀▄    
    █ ███ █ ██▄▄█ ▀▀▄██▄██▀▀▀▄█ ▀    
    █ ▀▀▀ █ ▀██▄█▀███▀▄▀█▄▀ █ ▀█     
    ▀▀▀▀▀▀▀ ▀▀ ▀▀▀   ▀   ▀  ▀▀▀      
Scan the QR code above to get the file on your phone.
If it does not work, try the --browser-display option.

Press CTRL+C to exit once you get the file.
```

In case your terminal does not render the QR code properly, try the `-b` option to
get an SVG image to open in your browser:

```
➜ share-file-qr -b README.md
Click on this SVG image link to display the QR code to scan:
http://192.168.0.2:4000/qrcode.svg

Press CTRL+C to exit once you got the file.
```

At this point, you should have a QR code displayed directly in your terminal, or in
your computer's browser as an SVG image.

Once you have a QR code (either directly from the terminal or from your computer's
browser) scan it with your smartphone to get a URL to the file and download it in
your web browser. Depending on your phone's OS you may have to scan the QR
code differently:
* iOS, use the standard camera app
* Android: try [QR Code Scanner](https://play.google.com/store/apps/details?id=me.scan.android.client)
  by [Scan](https://www.scan.me/)

## License

GPLv3

## Authors

This Python tool was implemented by [Pierre Walch](http://pwal.ch),
based on ideas from a Go project by [Claudio d'Angelis](https://github.com/claudiodangelis/qr-filetransfer).
