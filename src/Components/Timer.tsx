import { DateTime } from 'luxon';
import { useEffect, useState } from 'react';

interface PropType {
    roundEndsAt: Date | null;
}

export default function Timer(props: PropType) {
    const DEFAULT_TIMER_STRING = 'Shuffle the board to start';
    const { roundEndsAt } = props;
    const [timerString, setTimerString] =
        useState<string>(DEFAULT_TIMER_STRING);
    const [warning, setWarning] = useState<boolean>(false);

    const calculateTimerString = (val: Date) => {
        const luxDate = DateTime.fromJSDate(val);
        const diff = luxDate.diff(DateTime.now(), ['minutes', 'seconds']);
        if (diff.minutes < 0 || diff.seconds < 0) {
            return '0m 00s';
        }
        return `${diff.minutes}m ${Math.ceil(diff.seconds)
            .toString()
            .padStart(2, '0')}s`;
    };

    useEffect(() => {
        const timerInterval = setInterval(() => {
            let newTimerString: string;
            if (!roundEndsAt) {
                newTimerString = DEFAULT_TIMER_STRING;
            } else {
                newTimerString = calculateTimerString(roundEndsAt);
            }
            setTimerString(newTimerString);
            if (newTimerString === '0m 00s') {
                setWarning((prev) => !prev);
            }
        }, 1000);

        return () => clearInterval(timerInterval);
    }, [props.roundEndsAt]);

    return (
        <div className={`${warning ? 'text-red-500' : ''} text-2xl font-bold`}>
            {timerString}
        </div>
    );
}
