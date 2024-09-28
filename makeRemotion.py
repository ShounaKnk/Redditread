import csv
import random

def generate_remotion_code(csv_file):
    # Read data from CSV file
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    # Select a random post from the data
    post = random.choice(data)
    title = post[0]
    comments = post[1:]

    # Generate the Remotion React code
    code = f"""
import {{Composition}} from 'remotion';
import {{getAudioDurationInSeconds}} from '@remotion/media-utils';
import {{useCallback, useEffect, useState}} from 'react';
import {{continueRender, delayRender}} from 'remotion';

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
    return (
        <div style={{{{backgroundColor: '#1a1a1a', width: '100%', height: '100%', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', padding: '20px'}}}}>
            <h1 style={{PostTitle}}>{{title}}</h1>
            <SpeechSynthesis text={{title}} />
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
csv_file = 'your_reddit_data.csv'  # Replace with your CSV file path
remotion_code = generate_remotion_code(csv_file)

# Save the generated code to a file
with open('RedditReel.jsx', 'w') as file:
    file.write(remotion_code)

print("Remotion React code has been generated and saved to RedditReel.jsx")