module.exports = {
  testEnvironment: 'jsdom',
  setupFilesAfterEnv: ['@testing-library/jest-dom'],
  moduleNameMapper: {
    '^@/(.*)$': '<rootDir>/src/$1',
  },
  testPathIgnorePatterns: ['/node_modules/', '/.next/', '/cypress/', '/tests/integration/'],
  transform: {
    '^.+\.(ts|tsx)$': 'babel-jest',
  },
};
