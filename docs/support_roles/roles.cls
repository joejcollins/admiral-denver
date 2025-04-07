% Class Identification
\ProvidesClass{roles}[2023/12/14 Custom Class for Support Roles]

% Base Class
\LoadClass[a4paper,12pt]{article}

% Packages
\usepackage[british]{babel}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{hyperref}  % Required for hyperlinks
\usepackage[english]{isodate}
\usepackage{graphicx}
\usepackage{float}

% Make it look kind of like MS Word
\usepackage[margin=1in]{geometry}
\providecommand{\tightlist}{%  This command is in the pandoc template
  \setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\raggedright
\renewcommand{\familydefault}{\sfdefault}
\setlength{\parindent}{0pt}  % No indentation for paragraphs
\setlength{\parskip}{1em}  % Add space between paragraphs

\endinput
