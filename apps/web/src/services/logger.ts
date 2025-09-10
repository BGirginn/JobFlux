export const frontendLogger = {
  info: (message: string, context?: Record<string, unknown>) => {
    console.log(`[INFO] ${message}`, context);
    // TODO: Send logs to backend endpoint
  },
  error: (message: string, error: unknown, context?: Record<string, unknown>) => {
    console.error(`[ERROR] ${message}`, error, context);
    // TODO: Send logs to backend endpoint
  },
};
