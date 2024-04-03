import { DateTime } from 'luxon';
import {
    ChangeEventHandler,
    KeyboardEventHandler,
    useEffect,
    useState,
} from 'react';
import BoardSizeSelector from '../Components/BoardSizeSelector';
import BoggleBoard from '../Components/BoggleBoard';
import Timer from '../Components/Timer';
import MainLayout from '../Layouts/MainLayout';
import { BoardSizeType, findWord, getBoardLayout } from '../Utils';

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
                <div className="text-2xl">Boggled</div>
                <BoardSizeSelector
                    handleBoardSizeChange={handleBoardSizeChange}
                />
                <div className="flex items-center mb-4">
                    <input
                        id="allow-diagonals"
                        type="checkbox"
                        value=""
                        className="w-4 h-4 text-blue-600 bg-gray-100 border-gray-300 rounded focus:ring-blue-500 dark:focus:ring-blue-600 dark:ring-offset-gray-800 focus:ring-2 dark:bg-gray-700 dark:border-gray-600"
                        onChange={handleDiagonalClick}
                        checked={allowDiagonal}
                    />
                    <label
                        htmlFor="allow-diagonals"
                        className="ms-2 text-sm font-medium text-gray-900 dark:text-gray-300"
                    >
                        Allow diagonals?
                    </label>
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
                <div className="flex items-end gap-4">
                    <label
                        htmlFor="lookup"
                        className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
                    >
                        Lookup
                    </label>
                    <input
                        type="text"
                        id="lookup"
                        className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
                        required
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
