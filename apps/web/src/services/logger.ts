export const frontendLogger = {
  info: (message: string, context?: Record<string, any>) => {
    console.log(`[INFO] ${message}`, context);
    // TODO: Send logs to backend endpoint
  },
  error: (message: string, error: any, context?: Record<string, any>) => {
    console.error(`[ERROR] ${message}`, error, context);
    // TODO: Send logs to backend endpoint
  },
};
