import winston from 'winston';

export const logger = winston.createLogger({
  // 운영 환경에서는 info 이상만 출력해 로그 노이즈를 줄인다
  level: process.env.NODE_ENV === 'production' ? 'info' : 'debug',
  format: winston.format.combine(
    winston.format.timestamp({ format: 'YYYY-MM-DD HH:mm:ss' }),
    winston.format.colorize(),
    // 출력 형식: 2026-06-28 13:00:00 [info] 메시지
    winston.format.printf(({ timestamp, level, message }) => `${timestamp} [${level}] ${message}`),
  ),
  transports: [new winston.transports.Console()],
});
