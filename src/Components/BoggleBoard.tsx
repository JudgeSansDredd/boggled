import { BOARD_SIZES, BoardSizeType } from '../Utils';
import BoggleDie from './BoggleDie';

interface PropType {
    boardLayout: string[];
    highlightPath: number[];
    boardSize: BoardSizeType;
}

export default function Boggleboard(props: PropType) {
    const boardSize = BOARD_SIZES[props.boardSize];
    let gridRows = 'grid-rows-3';
    let gridCols = 'grid-cols-3';
    if (boardSize === 5) {
        gridRows = 'grid-rows-5';
        gridCols = 'grid-cols-5';
    } else if (boardSize === 6) {
        gridRows = 'grid-rows-6';
        gridCols = 'grid-cols-6';
    }

    const dice = props.boardLayout.map((d, i) => {
        return (
            <BoggleDie
                letter={d}
                key={`boggle-die-${i}`}
                highlighted={props.highlightPath.includes(i)}
            />
        );
    });

    return <div className={`grid ${gridRows} ${gridCols} gap-2`}>{dice}</div>;
}
