import React from 'react';
import { BOARD_SIZES } from '../Utils';

interface PropType {
  handleBoardSizeChange: (e: React.ChangeEvent<HTMLSelectElement>) => void;
}

export default function BoardSizeSelector({ handleBoardSizeChange }: PropType) {
  return (
    <div className="max-w-72">
      <label
        htmlFor="board-size"
        className="block mb-2 text-sm font-medium text-gray-900 dark:text-white"
      >
        Select an option
      </label>
      <select
        id="board-size"
        className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        onChange={handleBoardSizeChange}
      >
        <option value="big">
          {BOARD_SIZES.big} x {BOARD_SIZES.big}
        </option>
        <option value="superbig">
          {BOARD_SIZES.superbig} x {BOARD_SIZES.superbig}
        </option>
      </select>
    </div>
  );
}
