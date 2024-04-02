import { DateTime } from 'luxon';
import {
    ChangeEventHandler,
    KeyboardEventHandler,
    useEffect,
    useState,
} from 'react';
import BoggleBoard from '../Components/BoggleBoard';
import Timer from '../Components/Timer';
import MainLayout from '../Layouts/MainLayout';
import { BOARD_SIZES, BoardSizeType, findWord, getBoardLayout } from '../Utils';

export default function Board() {
    const [boardLayout, setBoardLayout] = useState<string[]>([
        ...'abcdefghijklmnopqrstuvwxy'.toUpperCase(),
    ]);
    const [lookupInputValue, setLookupInputValue] = useState<string>('');
    const [highlightPath, setHighlightPath] = useState<number[]>([]);
    const [lookupStatus, setLookupStatus] = useState<{
        working: boolean;
        definitionString: string;
    }>({ working: false, definitionString: '' });
    const [roundEndsAt, setRoundEndsAt] = useState<Date | null>(null);
    const [boardSize, setBoardSize] = useState<BoardSizeType>('big');
    const [allowDiagonal, setAllowDiagnoal] = useState<boolean>(false);

    const shuffleHandler = () => {
        setLookupInputValue('');
        const newLayout = getBoardLayout(boardSize);
        setBoardLayout(newLayout);
        setLookupStatus({ working: false, definitionString: '' });
        setRoundEndsAt(DateTime.now().plus({ minutes: 3 }).toJSDate());
    };

    const handleInputChange: ChangeEventHandler<HTMLInputElement> = (e) => {
        setLookupInputValue(e.currentTarget.value.toUpperCase());
    };

    const handleBoardSizeChange: ChangeEventHandler<HTMLSelectElement> = (
        e
    ) => {
        setBoardSize(e.currentTarget.value as BoardSizeType);
    };

    const handleInputKeyDown: KeyboardEventHandler<HTMLInputElement> = async ({
        key,
    }) => {
        if (key === 'Enter') {
            // TODO: Try to look up the word
        } else if (key === 'Escape') {
            setLookupInputValue('');
            setLookupStatus({ working: false, definitionString: '' });
        }
    };

    const handleDiagonalClick: ChangeEventHandler<HTMLInputElement> = (e) => {
        setAllowDiagnoal(e.currentTarget.checked);
    };

    useEffect(() => {
        const result = findWord(
            lookupInputValue,
            boardLayout,
            boardSize,
            allowDiagonal,
            []
        );
        if (result) {
            setHighlightPath(result);
        } else {
            setHighlightPath([]);
        }
    }, [boardLayout, lookupInputValue, allowDiagonal, boardSize]);

    return (
        <MainLayout pageName="Board">
            <div className="flex flex-col items-center gap-4 mt-4">
                <div className="text-2xl text-blue-700">Boggled</div>
                <select onChange={handleBoardSizeChange}>
                    <option value="big">
                        {BOARD_SIZES.big} x {BOARD_SIZES.big}
                    </option>
                    <option value="superbig">
                        {BOARD_SIZES.superbig} x {BOARD_SIZES.superbig}
                    </option>
                </select>
                <div className="flex">
                    <div>Allow Diagonals?</div>
                    <input
                        type="checkbox"
                        checked={allowDiagonal}
                        onChange={handleDiagonalClick}
                    />
                </div>
                <Timer roundEndsAt={roundEndsAt} />
                <BoggleBoard
                    boardLayout={boardLayout}
                    highlightPath={highlightPath}
                    boardSize={boardSize}
                />
                <button
                    className="p-2 bg-blue-300 rounded-full hover:bg-blue-400"
                    onClick={shuffleHandler}
                >
                    Shuffle
                </button>
                <div className="flex items-center gap-4">
                    <div>Lookup</div>
                    <input
                        className="rounded-md"
                        type="text"
                        name="lookup"
                        id="lookup"
                        value={lookupInputValue}
                        onChange={handleInputChange}
                        onKeyDown={handleInputKeyDown}
                    />
                </div>
                {!lookupStatus.working && (
                    <div className="p-2 mx-4">
                        {lookupStatus.definitionString}
                    </div>
                )}
            </div>
        </MainLayout>
    );
}
