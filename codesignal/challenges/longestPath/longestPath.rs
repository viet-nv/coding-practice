fn longestPath(fileSystem: String) -> i32 {
    let mut stack: Vec<String> = Vec::new();
    let lines: Vec<&str> = fileSystem.split('\u{C}').collect();

    let mut curlen = 0;
    for name in lines {
        let fileName = name.replace('\t', "");
        let level = name.len() - fileName.len();

        if stack.len() > 0 {
            while level < stack.len() {
                stack.pop();
            }
        }
        stack.push((*fileName).to_string());

        let mut len = stack.len() - 1;
        for s in &stack {
            len += s.len();
        }

        if fileName.contains('.') && len > curlen {
            curlen = len
        }
    }

    return curlen as i32;
}

