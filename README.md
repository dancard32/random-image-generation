# website

## Description

This project is to display my skills as both a programmer and an engineer, and is my first project using React. This was based upon the base site by [harikanani](https://github.com/harikanani), [BraydenTW](https://github.com/BraydenTW), and [shishirtiwari23](https://github.com/shishirtiwari23) and adapted to fit my dual-role skills of being both an aerospace engineer and a computer scientist.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)

## Installation

All that's required is having _npm_ installed locally on your machine, and the ability to create _react-app_ with _npx_

## Usage

### Running locally

To start a _localhost_ website to allow offline edits, use the following command in the terminal

```
npm start
```

This will create a build of the site and any saves locally will automatically refresh the page and result in an updated website.

### Deploying on Github Pages

If you would like to re-create this project and use Github pages to host your portfolio, this template is essentially ready to go with a minor change.

<br />

You must install _gh-pages_ module through _npm_, to install use the following:

```
npm install gh-pages --save-dev
```

Then you'll need to edit _homepage_ from the _package.json_ file which is located in the root directory to the url of your Github Pages website.

```
"homepage": "http://DanCard32.github.io/website",
```

To deploy use the following command

```
npm run deploy
```

Push these changes to your main branch and the changes on the website should appear shortly thereafter with a short delay

## Credits

Special thanks to:

- [harikanani](https://github.com/harikanani)
- [BraydenTW](https://github.com/BraydenTW)
- [shishirtiwari23](https://github.com/shishirtiwari23)

For creating a phenomenal website and allowing use of it for personal use. Although I have tailored it to my own liking, it is largely thanks to them that I have my first functioning website!

---

## MIT License

Copyright (c) 2021 harikrushn kanani

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
