import 'dotenv/config';
import express from 'express';
import passport from 'passport';
import path from 'path';
import { prisma } from './lib/prisma';
import { logger } from './lib/logger';
import authRouter from './routes/auth';
import meRouter from './routes/me';
import viewRouter from './routes/view';

const app = express();
const PORT = process.env.PORT ?? 3000;

// EJS를 뷰 엔진으로 등록
// __dirname은 ts-node-dev 실행 시 src/, 컴파일 후 실행 시 dist/ 를 가리키므로
// views/ 디렉토리는 항상 ../views로 참조한다
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, '../views'));

app.use(express.json());
// passport.initialize()는 요청마다 req.user를 초기화한다
// session: false 전략을 쓰더라도 반드시 필요하다
app.use(passport.initialize());

app.use('/auth', authRouter);
app.use('/me', meRouter);
app.use('/', viewRouter);

app.listen(PORT, async () => {
  try {
    // 서버 시작 시 DB 연결을 명시적으로 확인한다
    // Prisma는 첫 쿼리 시 자동으로 연결하지만, 설정 오류를 조기에 잡기 위해 직접 호출한다
    await prisma.$connect();
    logger.info('DB connected');
  } catch (e) {
    logger.error(`DB connection failed: ${e}`);
    process.exit(1);
  }
  logger.info(`Server running on http://localhost:${PORT}`);
});
