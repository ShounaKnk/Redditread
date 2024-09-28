import csv
import random

def generate_remotion_code(csv_file):
    # Read data from CSV file
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Select a random post from the data
    post = random.choice(data)
    author = post[0]
    title = post[1]
    comments = post[2:]

    # Generate the Remotion React code
    code = f"""
import {{Composition}} from 'remotion';
import {{getAudioDurationInSeconds}} from '@remotion/media-utils';
import {{useCallback, useEffect, useState}} from 'react';
import {{continueRender, delayRender}} from 'remotion';

const AuthorText = {{fontSize: '28px', fontWeight: 'bold', textAlign: 'center', color: 'white', marginBottom: '10px'}};
const PostTitle = {{fontSize: '24px', fontWeight: 'bold', textAlign: 'center', color: 'white'}};
const CommentText = {{fontSize: '20px', textAlign: 'center', color: 'white'}};

const SpeechSynthesis = ({{text}}) => {{
    const [handle] = useState(() => delayRender());
    const [duration, setDuration] = useState(1);

    const getDuration = useCallback(async () => {{
        setDuration(await getAudioDurationInSeconds(text));
        continueRender(handle);
    }}, [handle, text]);

    useEffect(() => {{
        getDuration();
    }}, [getDuration]);

    return (
        <audio src={{`https://api.streamelements.com/kappa/v2/speech?voice=Brian&text=${{encodeURIComponent(text)}}`}} />
    );
}};

export const MyComposition = () => {{
    const author = "{author}";
    const title = "{title}";
    const comments = {comments};

    return (
        <Composition
            id="MyComp"
            component={{MyComp}}
            durationInFrames={{60 * 30}} // 30 fps for 60 seconds
            fps={{30}}
            width={{1080}}
            height={{1920}}
        />
    );
}};

const MyComp = () => {{
    const author = "{author}";
    const title = "{title}";
    const fullText = `${{author}} posted ${{title}}`;

    return (
        <div style={{{{backgroundColor: '#1a1a1a', width: '100%', height: '100%', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', padding: '20px'}}}}>
            <div>
                <h2 style={{AuthorText}}>{{author}}</h2>
                <h1 style={{PostTitle}}>{{title}}</h1>
            </div>
            <SpeechSynthesis text={{fullText}} />
            {{comments.map((comment, index) => (
                <div key={{index}} style={{{{marginTop: '20px'}}}}>
                    <p style={{CommentText}}>{{comment}}</p>
                    <SpeechSynthesis text={{comment}} />
                </div>
            ))}}
        </div>
    );
}};
"""

    return code

# Usage
csv_file = 'cmmnts.csv'  # Replace with your CSV file path
remotion_code = generate_remotion_code(csv_file)

# Save the generated code to a file
with open('RedditReel.jsx', 'w') as file:
    file.write(remotion_code)

print("Remotion React code has been generated and saved to RedditReel.jsx")