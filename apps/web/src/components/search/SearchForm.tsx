import React from 'react';

const SearchForm: React.FC = () => {
  return (
    <form className="bg-white p-6 rounded-lg shadow-md">
      <div className="mb-4">
        <label htmlFor="title" className="block text-gray-700 text-sm font-bold mb-2">
          Job Title
        </label>
        <input
          type="text"
          id="title"
          name="title"
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          placeholder="e.g., Software Engineer"
        />
      </div>
      <div className="mb-4">
        <label htmlFor="location" className="block text-gray-700 text-sm font-bold mb-2">
          Location
        </label>
        <input
          type="text"
          id="location"
          name="location"
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          placeholder="e.g., London"
        />
      </div>
      <button
        type="submit"
        className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
      >
        Search
      </button>
    </form>
  );
};

export default SearchForm;
