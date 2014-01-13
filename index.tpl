<!DOCTYPE>
<head>
    <title>dmpete.rs</title>
    <meta name="description" content="the personal website of dmpeters">
    <meta name="keywords" content="dmpeters, dmpete.rs, _dmpeters, david peters, david m peters, dave peters, dave, david, peters">
    <meta name="author" content="david peters">
    <meta charset="utf-8">
    <link rel="stylesheet" title="Ascetic" href="reset.css">
    <link rel="stylesheet" title="Ascetic" href="ascetic.css">
    <style>
        body {font: small Arial, sans-serif; border-top: 3px solid black;}
        header {padding-left: 100px;}
        h2 {font: bold 100% Arial, sans-serif; margin-top: 2em; margin-bottom: 0.5em;}
        ul {margin: 0; padding: 0;}
        li {display: inline;}
        pre {margin: 0; font-size: medium;}
    </style>
    <script src="highlight.pack.js"></script>
    <script>
        hljs.tabReplace = '    ';
        hljs.initHighlightingOnLoad();
    </script>
</head>
<body>
    <div id="page">
        <header>
            <h2>dmpete.rs</h2>
            <nav>
                <ul id="nav">
                    <li>[<a href="#">about</a>,</li>
                    <li><a href="https://github.com/dmpeters">github</a>,</li>
                    <li><a href="http://www.linkedin.com/in/dmpeters">linkedin</a>,</li>
                    <li><a href="mailto:dmpeters63@gmail.com">contact</a>]</li>
                </ul>
            </nav>
        </header>

        <section>
            <div id="json">
            <pre><code>
            {
              %for o in obj:
              "{{o}}": "{{obj[o]}}",
              %end
            }
            </code></pre>
            </div>
        </section>

        <footer>
            &nbsp;
        </footer>

    </div>
</body>
