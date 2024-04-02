interface PropType {
    letter: string;
    highlighted: boolean;
}

export default function BoggleDie(props: PropType) {
    const { letter, highlighted } = props;
    const bgColor = highlighted ? 'bg-green-400' : 'bg-white';
    let displayedLetter: string;
    if (letter === 'Q') {
        displayedLetter = 'Qu';
    } else if (letter === '.') {
        displayedLetter = '⬛️';
    } else if (letter.length === 2) {
        displayedLetter = `${letter.charAt(0).toUpperCase()}${letter
            .charAt(1)
            .toLowerCase()}`;
    } else {
        displayedLetter = letter;
    }
    return (
        <div
            className={`flex items-center justify-center w-16 h-16 ${bgColor} border-2 border-black rounded-md`}
        >
            <div className="text-2xl text-black ">{displayedLetter}</div>
        </div>
    );
}
