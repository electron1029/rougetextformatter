'''
Created on Sep 21, 2015

@author: cfry
'''

import os
rootdir = '/Volumes/My Passport for Mac/Dropbox/school files/CSUPomona/691 F15/RELEASE-1.5.5/test/models'
newFileText = ''
numLines = 0;

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if ('DS_Store' in file):
            continue;
        f = open(os.path.join(subdir, file), 'r');
        newFileText += '<html>\n';
        newFileText += '<head><title>' + file + '</title></head>\n';
        newFileText += '<body>';
        line = f.readline();
        while (line):
            numLines = numLines + 1;
            newFileText += '\n<a name="' + str(numLines) + '">[' + str(numLines) +\
                ']</a> <a href="#' + str(numLines) + '" id=' + str(numLines) + '>' + line.rstrip('\n') + '</a>';
            line = f.readline();
        numLines = 0;
        newFileText += '</body>\n';
        newFileText += '</html>';
        f.close();
        f2 = open(os.path.join(subdir, file), 'w');
        f2.write(newFileText);
        f2.close();
        newFileText = '';