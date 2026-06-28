import { Router, Request, Response } from 'express';

const router = Router();

// 로그인 페이지를 렌더링한다
router.get('/', (_req: Request, res: Response) => {
  res.render('index');
});

// Google OAuth 콜백 후 리다이렉트되는 페이지
// auth 라우터에서 /callback?token=... 으로 리다이렉트하면 이 핸들러가 받는다
// token을 EJS 템플릿에 전달해 화면에 표시한다
router.get('/callback', (req: Request, res: Response) => {
  const token = req.query.token as string;
  res.render('callback', { token });
});

export default router;
