import express, { Request, Response, NextFunction, RequestHandler } from 'express';

const app = express();
app.use(express.json());

// 글로벌 로거
app.use((req: Request, _res: Response, next: NextFunction) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.path}`);
  next();
});

// RequestHandler: (req, res, next) => void 의 타입 별칭
// 미들웨어 함수를 변수로 분리할 때 유용
const authMiddleware: RequestHandler = (req, res, next) => {
  const token = req.headers['authorization'];
  if (!token) {
    res.status(401).json({ message: 'Unauthorized' });
    return; // return next() 대신 명시적 return으로 이후 코드 차단
  }
  // req.user는 types/express.d.ts에서 확장했기 때문에 타입 에러 없음
  req.user = { id: 1, name: '홍길동' };
  next();
};

app.get('/protected', authMiddleware, (req: Request, res: Response) => {
  res.json({ user: req.user });
});

app.get('/public', (_req: Request, res: Response) => {
  res.json({ message: '누구나 접근 가능' });
});

app.get(
  '/chain',
  (req: Request, _res: Response, next: NextFunction) => { req.step1 = true; next(); },
  (req: Request, _res: Response, next: NextFunction) => { req.step2 = true; next(); },
  (req: Request, res: Response) => { res.json({ step1: req.step1, step2: req.step2 }); },
);

app.listen(3000, () => console.log('http://localhost:3000'));
