
import {Composition} from 'remotion';
import {getAudioDurationInSeconds} from '@remotion/media-utils';
import {useCallback, useEffect, useState} from 'react';
import {continueRender, delayRender} from 'remotion';

const AuthorText = {fontSize: '28px', fontWeight: 'bold', textAlign: 'center', color: 'white', marginBottom: '10px'};
const PostTitle = {fontSize: '24px', fontWeight: 'bold', textAlign: 'center', color: 'white'};
const CommentText = {fontSize: '20px', textAlign: 'center', color: 'white'};

const SpeechSynthesis = ({text}) => {
    const [handle] = useState(() => delayRender());
    const [duration, setDuration] = useState(1);

    const getDuration = useCallback(async () => {
        setDuration(await getAudioDurationInSeconds(text));
        continueRender(handle);
    }, [handle, text]);

    useEffect(() => {
        getDuration();
    }, [getDuration]);

    return (
        <audio src={`https://api.streamelements.com/kappa/v2/speech?voice=Brian&text=${encodeURIComponent(text)}`} />
    );
};

export const MyComposition = () => {
    const author = "u/PizzaBliAnanas";
    const title = "People who left their religion, what was the final straw that made you leave?";
    const comments = ['Asking me for a paystub to verify I was actually tithing 10%. Pastor was driving a new Cadillac. Gtfo', 'tbh, I left when I noticed that my ‘community’ felt more like a ‘judgmental audience’!'];

    return (
        <Composition
            id="MyComp"
            component={MyComp}
            durationInFrames={60 * 30} // 30 fps for 60 seconds
            fps={30}
            width={1080}
            height={1920}
        />
    );
};

const MyComp = () => {
    const author = "u/PizzaBliAnanas";
    const title = "People who left their religion, what was the final straw that made you leave?";
    const fullText = `${author} posted ${title}`;

    return (
        <div style={{backgroundColor: '#1a1a1a', width: '100%', height: '100%', display: 'flex', flexDirection: 'column', justifyContent: 'center', alignItems: 'center', padding: '20px'}}>
            <div>
                <h2 style={AuthorText}>{author}</h2>
                <h1 style={PostTitle}>{title}</h1>
            </div>
            <SpeechSynthesis text={fullText} />
            {comments.map((comment, index) => (
                <div key={index} style={{marginTop: '20px'}}>
                    <p style={CommentText}>{comment}</p>
                    <SpeechSynthesis text={comment} />
                </div>
            ))}
        </div>
    );
};
